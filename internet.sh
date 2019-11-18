#!/bin/bash
ON="0"
OFF="1"
MODEM=29
echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "Você está: Online ;)"
else
    if [ !$MODEM_STATUS ];
        then
            echo "Você está: Offline :("
            echo "Desligando Modem..."
            export MODEM_STATUS true
            gpio -g write $MODEM $OFF
            echo "Sleep, pretty darling, do not cry."
            echo "And I will sing a lullaby..."
            echo "ZzzZZzzZZZ"
            sleep 60
            echo "WAKE UP! Put a little makeup!"
            gpio -g write $MODEM $ON
            unset MODEM_STATUS
        else
            echo "Modem está reiniciando..."
            export MODEM_STATUS true
        fi


fi