while(true) do
   sleep 10;
   echo `date +"%H:%M:%S"` "log text" >> /tmp/server.log
done;
