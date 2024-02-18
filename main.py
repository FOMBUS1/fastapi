from fastapi import FastAPI
from cproc import cproc
from fs import fs
from ijulia import ijulia

app = FastAPI()

app.include_router(
                cproc.router,
                prefix='',
                tags=['cproc']
                )

app.include_router(
                fs.router, 
                prefix='',
                tags=['fs']
                )

app.include_router(
                ijulia.router,
                prefix='',
                tags=['ijulia']
)