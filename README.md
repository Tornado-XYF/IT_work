# IT_work

作业在test01
下载整个文件夹后，运行main.py文件
访问`http://127.0.0.1:11451/hello`即可查看返回值

调试resiner和login接口，可以隐去

```.
import uvicorn
uvicorn.run(app, host="127.0.0.1", port=11451)
```
然后访问`http://127.0.0.1:8000/docs`，在swagger UI中进行调试
