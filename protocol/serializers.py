from rest_framework import serializers

from protocol.models import MetamaskAccount, Transaction, IPFS


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetamaskAccount
        fields = ['user_wallet_address']


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['res_hash', 'account']


class IPFSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPFS
        fields = ['result_hash', 'account']


