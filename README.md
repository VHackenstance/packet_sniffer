<h4>Packet Sniffer</h4>
<p><b>Capture</b> data flowing through an interface</p>
<p><b>Filter</b> this data</p>
<p>Display interesting information such as:</p>
<ol>
<li>Login Credentials (usernames and <b>passwords</b>).</li>
<li>Visited <b>websites</b>.</li>
<li>Images.</li>
<li>....etc</li>
</ol>
<h3>packet_sniffer</h3>
<h4><i>Capture and Filter Data</i></h4>
<ol>
<li><b>Scapy</b> has a sniffer function, <b>sniff</b>.</li>
<li>Sniff can capture data sent and from an <b>iface</b> (interface).</li>
<li>It can call a function given to the <b>prn</b> field on each packet</li>
</ol>
<h4>Syntax:</h4>
<p>from scapy.all import sniff</p>
<p>scapy.sniff(iface=[INTERFACE], prn=[CALL_BACK_FUNCTION])</p>
<br/>
<h4>Testing a http only site with WebGoat</h4>
<p>I have created an early testing build file, to use this:</p>
<p>Install with Docker, <br/>
sudo apt update <br/>
sudo apt install -y docker.io <br/>  
<b>Do not install podman it is a tag buggy</b><br/>
sudo systemctl enable docker --now<br/>

after installing Docker: <br/>
<b>docker run -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 -e TZ=Europe/Amsterdam webgoat/webgoat </b>
</p>
<p>
Error message: Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg <br/>
Solution: touch /etc/containers/nodocker
</p>
<p>
Error message: Multiple <br/>
Solution: Everything was solved by uninstalling docker-podman and rein
stalling docker.io
</p>
<ol>
<li>Navigate to: /etc/containers/registries.conf</li>
<li>Open with text editor and add the line: unqualified-search-registries = ["docker.io"]   </li>
<li>sudo podman run docker.io/webgoat/webgoat   </li>
<li>Password for admin: YmU1ZTdlNWEtMWE4Yi00NmRiLWI1MjAtOGMzNDEzNGU2NzE5</li>
</ol>

<p>https://owasp.org/www-project-webgoat/</p>

<h4>To Test WebGoat Locally withing Kali</h4>
<p>Use port <b>lo</b> as this is a loop back.</p>
<p>Run WebGoat:  <b>sudo docker run -p 8080:8080 webgoat/webgoat</b></p>
<p>WebGoat UI/site is at: <b>http://localhost:8080/WebGoat</b></p>
<p>Helper WebWolf UI/site is at: <b>http://localhost:9090/WebWolf</b></p>

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

