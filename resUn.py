a = '''dpkg: warning: while removing bbb-apps, directory '/usr/share/red5/webapps/bigbluebutton' not empty so not removed
dpkg: warning: while removing bbb-webrtc-sfu, directory '/usr/local/bigbluebutton/bbb-webrtc-sfu/config' not empty so not removed
dpkg: warning: while removing bbb-webrtc-sfu, directory '/usr/local/bigbluebutton/bbb-webrtc-sfu/node_modules/sip.js/node_modules/ws' not empty so not removed
dpkg: warning: while removing bbb-apps-akka, directory '/var/log/bbb-apps-akka' not empty so not removed
dpkg: warning: while removing bbb-apps-screenshare, directory '/usr/share/red5/webapps/screenshare' not empty so not removed
dpkg: warning: while removing bbb-apps-sip, directory '/usr/share/red5/webapps/sip' not empty so not removed
dpkg: warning: while removing bbb-apps-video, directory '/usr/share/red5/webapps/video' not empty so not removed
dpkg: warning: while removing bbb-apps-video-broadcast, directory '/usr/share/red5/webapps/video-broadcast' not empty so not removed
dpkg: warning: while removing bbb-client, directory '/var/www/bigbluebutton/client' not empty so not removed
dpkg: warning: while removing bbb-etherpad, directory '/usr/share/etherpad-lite/var' not empty so not removed
dpkg: warning: while removing bbb-etherpad, directory '/usr/share/etherpad-lite/src' not empty so not removed
dpkg: warning: while removing bbb-etherpad, directory '/usr/share/etherpad-lite/node_modules/ep_better_pdf_export' not empty so not removed
dpkg: warning: while removing bbb-freeswitch-core, directory '/opt/freeswitch/var/log/freeswitch' not empty so not removed
dpkg: warning: while removing bbb-freeswitch-core, directory '/opt/freeswitch/var/lib/freeswitch/db' not empty so not removed
dpkg: warning: while removing bbb-freeswitch-core, directory '/opt/freeswitch/etc/freeswitch/tls' not empty so not removed
dpkg: warning: while removing bbb-freeswitch-sounds, directory '/opt/freeswitch' not empty so not removed
dpkg: warning: while removing bbb-fsesl-akka, directory '/var/log/bbb-fsesl-akka' not empty so not removed
dpkg: warning: while removing bbb-record-core, directory '/var/bigbluebutton/captions' not empty so not removed
dpkg: warning: while removing bbb-record-core, directory '/var/bigbluebutton/recording/status' not empty so not removed
dpkg: warning: while removing bbb-record-core, directory '/usr/local/bigbluebutton' not empty so not removed
dpkg: warning: while removing bbb-red5, directory '/var/log/red5' not empty so not removed
dpkg: warning: while removing bbb-red5, directory '/var/cache/red5/work' not empty so not removed
dpkg: warning: while removing bbb-red5, directory '/var/lib/red5/webapps' not empty so not removed
dpkg: warning: while removing bbb-red5, directory '/usr/share/red5' not empty so not removed
dpkg: warning: while removing bbb-transcode-akka, directory '/var/log/bbb-transcode-akka' not empty so not removed
dpkg: warning: while removing bbb-web, directory '/var/log/bigbluebutton' not empty so not removed
dpkg: warning: while removing bbb-web, directory '/var/bigbluebutton' not empty so not removed
dpkg: warning: while removing bbb-web, directory '/etc/bigbluebutton/nginx' not empty so not removed
dpkg: warning: while removing bbb-web, directory '/usr/share/bbb-web/WEB-INF/classes' not empty so not removed
dpkg: warning: while removing ruby2.3, directory '/var/lib/gems/2.3.0' not empty so not removed
dpkg: warning: while removing ruby-power-assert, directory '/usr/share/rubygems-integration/all' not empty so not removed
'''
a = a.splitlines()
from os import system
for i in a:
 i = i.split(' ')[6]
 print('Remove dir : '+str(i))
 system('rm -rf '+str(i))
