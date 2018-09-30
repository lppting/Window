#!bin/bash
lock="run.py"
#启动服务
start(){
        echo "service start..."
        su root -c "python /home/pi/run.py &"
}
#停止服务
stop(){
        echo "service stop..."
        pkill -f $lock
}
#查看服务状态
status(){
        if [ -e $lock ];then
            echo "$0 service start"
        else
            echo "$0 service stop"
        fi
}
#重新启动
restart(){
        stop
        start
}
case "$1" in
"start")
        start
        ;;
"stop")
        stop
        ;;
"status")
        status
        ;;
"restart")
        restart
        ;;
*)
        echo "$0 start|stop|status|restart"
        ;;
esac

