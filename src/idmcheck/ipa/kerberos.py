from idmcheck.ipa.plugin import IPAPlugin, registry


@registry
class IPAKerberosCheck(IPAPlugin):
    def check(self):
        pass
