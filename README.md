<h4>Packet Sniffer</h4>
<p><b>Capture</b> data flowing through an interface</p>
<p><b>Filter</b> this data</p>
<p>Display:</p>
<ol>
<li>Login Credentials (usernames and passwords).</li>
<li>Visited <b>URLs</b>.</li>
<li>Images.</li>
<li>....etc</li>
</ol>
<h4>Arp_spoof + Packet_sniffer</h4>
<ol>
<li>Target a computer on the same Network</li>
<li>Make sure path forwarding is enabled</li>
<li>Set ip tables, from script set_iptables.py</li>
<li>Arp_spoof to redirect the flow of packets (OnPath, PitM)</li>
<li>Packet_sniffer to see <b>URLs</b>, <b>usernames</b> and <b>passwords</b> sent by target.</li>
<li>Flush ip_tables when finished.</li>
</ol>
<h4>The next phase in the project(s?)</h4>
<h5>Intercepting and Modifying Packets</h5>



