# picow_wol
Raspberry Pico W to wake up sleeping lan devices 

With a Raspberry Pico W you can easily set up an "on alarm" for your own WOL PC/devices. A Raspberry Pico W simply sends a Magic packet multiple times into the network. WOL capable devices recognize their own MAC address and wake up from their power-sucking deep sleep. In my own environment I use a NAS (network storage), which I don't need daily, but only when needed. On the device itself there is a button, if this is pressed, the NAS wakes up and is accessible/usable in the network after a short time. With the small Raspberry Pico W I can also wake up the NAS remotely. The small Micropython program creates the waking Magic packet and sends it as a broadcast to the network. I repeat the sending process three times. After the broadcast, I make the LED integrated on the Raspberry Pico blink permanently. This is the sign for me to take my finger off the power supply button again.
I would definitely urge you to think about the power consumption of your NAS. Even if it only uses 25 watts in idle mode, that would be 600 Wh a day. In the year these 365 * 0,6 KWh * 0,40 Euro = 87 senseless Euro. With my NAS there is even an option that the NAS automatically goes into sleep mode every day at xxxx o'clock. I wake up the NAS with the Raspberry Pico W when I need it and then it goes to sleep again automatically deep in the night (sleep mode).
Of course you can also use something like this with PC's that you only open via RDP connection from time to time.

The software is currently only designed for one device (MAC address). You can also wake up different devices in your network via WOL. A suitable circuit/software will follow. 

more info will follow and https://icplan.de
here you can find a description of WOL https://www.heise.de/tipps-tricks/Wake-on-LAN-was-ist-das-4585127.html


**************************************************************************************************************************************************

Mit einem Raspberry Pico W kann man sehr leicht einen "Auf Wecker" für seine eignen im Schalf liegenden WOL PC/Geräte aufbauen. Eine Raspberry Pico W sendet dazu einfach ein Magic Paket mehrfach in das Netzwerk. WOL taugliche Geräte erkennen die eigenen MAC-Adresse und wachen aus dem stromsprenden Tiefschlaf auf. In meinem eignen Umfeld verwende ich ein NAS (Netzwerkspeicher), welchen ich nicht täglich, sondern nur bei Bedarf benötige. Am Gerät selbst gibt es eine Taste, wird diese gedrückt, wacht das NAS auf und ist nach kurzer Zeit im Netzwerk erreich-/nutzbar. Mit dem kleinen Raspberry Pico W kann ich das NAS auch aus der Ferne aufwecken. Das kleine Micropython Programm erstellt das weckende Magic Paket und sendet es als Broadcast in das Netzwerk. Den Sendevorgang wiederhole ich dreimal. Nach der Sendung lasse ich die auf dem Raspberry Pico integrierte LED dauerhaft blinke. Das ist für mich das Zeichen, dass ich wieder den Finger von dem Taster der Spannungsversorgung nehmen kann.
Ich möchte Sie unbedingt auffordern über den Stromverbrauch Ihres NAS nachzudeneken. Auch wenn es nur im Idle Modus 25 Watt benötigt, wären das am Tag 600 Wh. Im Jahr kosten diese 365 * 0,6 KWh * 0,40 Euro = 87 sinnlose Euro. Bei meinem NAS gibt es sogar einen Möglichkeit, dass sich das NAS jeden Tag um xxxx Uhr automatisch in den Ruhezustand versetzt. Ich wecke das NAS mit dem Raspberry Pico W wenn ich es benötige und dann geht es wieder automatisch tief in der Nacht schlafen (Ruhezustand).
So etwas kann man natürlich auch mit PC's verwenden, die man nur ab und zu per RDP Verbindung öffnet.

Die Software ist momentan nur für ein auzuweckendes Gerät (MAC Adresse) geschieben. Problemlos kann auch verschiedenen Geräte in seinem Netzwerk über WOL wecken. Eine passende Schaltung/Software folgt. 

weitere Info folgen und https://icplan.de
hier finden Sie eine Beschreibung zum WOL https://www.heise.de/tipps-tricks/Wake-on-LAN-was-ist-das-4585127.html

