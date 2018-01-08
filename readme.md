## Raspberry Pi Velodyne Puck LITE Logger

# Description

Logs packet data collected from a Velodyne Puck LITE

# Setup

 * Install an operating system for your Raspberry Pi
   - I recommend Rasbian LITE or some other Debian variant
   - You will likely want to format the partition that you will be storing your collected data on to FAT32 so data can be easily retrieved from Windows and OS X
 * Establish and internet connection and install the necessary packages with
    ```
    sudo apt install python3-dev python3-rpi.gpio git
    ```
 * Clone the rpi-puck-logger repository
   - I recommend just putting it in your home directory
    ```
    cd ~
    git clone https://github.com/joshuabrockschmidt/rpi-puck-logger.git
    ```
 * *Optional*: Set directory for dumping data
   - By default, the directory for dumping data is "dump" inside the parent directory
   - This can be changed by changing ```$DUMPDIR``` in ```start.sh``` near the top of the file to your desired dump directory
 * Manual logging
   - If you want to start data logging manually, simply run ```start.sh``` with the name of the interface data is being streamed to. For example, if your interface is ```eth0```, run
    ```
    sudo ./start.sh eth0
    ```
   - A timestamped pcap file will be created in your dump directory
 * Setup auto-logging
   - Add a cron job
    ```
    sudo crontab -e
    ```
   - Add the following line
    ```
    @reboot $DIRECTORY/rpi-puck-logger/start.sh $INTERFACE
    ```
   - ```$DIRECTORY``` should be replaced with the location of ```rpi-puck-logger```, and ```$INTERFACE``` with the name of the interface you will be collecting data from
 * *Optional*: LED status indicator
   - You attach an LED circuit to a GPIO pin to receive feedback about logging status
     * The LED will turn on when logging has started
     * The LED will blink when something has gone wrong and logging has no commenced
   - The GPIO pin is 8 by default. But this can be changed by changing the variable ```GPIO``` at the top of ```led.py```.
     * Note that 3.3V is LED on and 0V is LED off. Design your circuit accordingly
