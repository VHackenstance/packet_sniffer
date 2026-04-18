<h4>Packet Sniffer</h4>
<p><b>Capture</b> the data flowing through an interface</p>
<p><b>Read</b> the packet data that has flowed through an interface</p>
<p><b>Filter</b> this data</p>
<p>Display interesting information such as:</p>
<ol>
<li>Login Credentials (usernames and <b>passwords</b>).</li>
<li>Visited <b>websites</b>.</li>
<li>Images.</li>
<li>....etc</li>
</ol>
<h4><i>Capture and Filter Data</i></h4>
<ol>
<li><b>Scapy</b> has a sniffer function called <b>sniff</b>.</li>
<li>Sniff can capture data sent and from an <b>iface</b> (interface).</li>
<li>It can call a function given to the <b>prn</b> field on each packet</li>
</ol>
<h4>Syntax:</h4>
<p>from scapy.all import sniff</p>
<p>scapy.sniff(iface=[INTERFACE], prn=[CALL_BACK_FUNCTION])</p>
<br/>>
<h4>Testing a http only site with WebGoat</h4>
<p>I have created an early testing build file, to use this:</p>
<p>I installed without an issue using Docker, after installing Docker hehe.</p>
<p>https://owasp.org/www-project-webgoat/</p>
<p>Use port lo as this is a loop back.</p>
<p>Run WebGoat:</p>
<p>sudo docker run -p 8080:8080 webgoat/webgoat</p>
<p>Seems to be working so far.</p>
<h4>Arp_spoof + Packet_sniffer</h4>
<ol>
<li>Target a computer on the same Network</li>
<li>Arp_spoof to redirect the flow of packets (OnPath, PitM)</li>
<li>Packet_sniffer to see <b>URLs</b>, <b>usernames</b> and <b>passwords</b> sent by target.</li>
</ol>
<h4>The next phase in the project(s?)</h4>
<h5>Intercepting and Modifying Packets</h5>
<ol>
    <li>Scapy can be used to:
        <ol>
            <li>Create Packets.</li>
            <li>Analyse packets.</li>
            <li>Send/recieve packets.</li>
        </ol>
    </li>
    <li>But it cannot be used to <b>intercept</b> packet/flows.</li>
</ol>

