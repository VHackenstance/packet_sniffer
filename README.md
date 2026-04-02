<h4>Packet Sniffer</h4>
<p><b>Capture</b> the data flowing through an interface</p>
<p><b>Read</b> the packet data that has flowed through an interface</p>
<p><b>Filter</b> this data</p>
<p>Display interesting information such as:</p>
<ol>
<li>Login Information (usernames and <b>passwords</b>).</li>
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

