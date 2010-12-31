import sys

nicks = (
'jujubeansR',
'cfgagk',
'klare80b',
'brbdad',
'root_at_PS',
'AvariceAnon',
'ais666',
'Djarki',
'jellejelleKANG',
'bovidelb',
'ChoccyBrown4',
'__Cybercrime__',
'SubcommandanteMarcos',
'culdesacsacs',
'KidPoke_her',
'DarkIsNotHere',
'zlighieri',
'docGZY',
'dullsklana',
'eagsleazy',
'enochlauz',
'skogskogskog',
'EVulashun',
'lustingre',
'galdfium',
'JDonato',
'ElephantWarfare',
'askjeevus',
'HighOnBTC',
'JohannoReeves7',
'jacophile',
'TsunamiOfMutilation',
'Pilliondude',
'jcmmccoy',
'renezzzzzz',
'SLOWPOKER',
'STS89',
'margaret_thatcher_anhero',
'beanerseatbeans',
'uint_64bit',
'gilese581g_2',
'wafuWafie',
'zhao'
)

print 'servers = ('
for i, n in enumerate(nicks):
    if i > 0:
        print ','
    print '  {'
    print '    address = "irc.freenode.org";'
    print '    chatnet = "Freenode%d";'%i
    print '    port = "6667";'
    print '    use_ssl = "no";'
    print '    ssl_verify = "no";'
    print '    autoconnect = "yes";'
    sys.stdout.write('  }')
print '\n);'

print 'chatnets = {'
for i, n in enumerate(nicks):
    print '  Freenode%d = {'%i
    print '    type = "IRC";'
    print '    nick = "%s";'%n
    print '    username = "%s";'%n
    print '    realname = "%s";'%n
    print '  };'
print '};'

print 'channels = ('
for i, n in enumerate(nicks):
    if i > 0:
        print ','
    sys.stdout.write('  { name = "#pokerface"; chatnet = "Freenode%d"; autojoin = "Yes"; }'%i)
print '\n);'
