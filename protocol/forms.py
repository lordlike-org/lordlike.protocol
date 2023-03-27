from django import forms

from protocol.models import Transaction, MetamaskAccount, IPFS
from protocol.validators import validate_file_size, validate_file_type, validate_file_content


class CreateTextTransForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('data',)


class UpdateTextTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('data',)


class ConnectWallet(forms.ModelForm):
    class Meta:
        model = MetamaskAccount
        fields = ('user_wallet_address',)


class IPFSTransForm(forms.ModelForm):
    class Meta:
        model = IPFS
        fields = ('file', 'text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].validators.extend([
            validate_file_size,
            validate_file_type,
            validate_file_content
        ])






