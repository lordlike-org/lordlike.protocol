from django import forms

from protocol.models import Transaction, MetamaskAccount, IPFS


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






