while(true) do
   sleep 1;
   echo `date +"%H:%M:%S"` "log text" >> /tmp/app.log
done;
