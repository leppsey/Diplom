from fastapi import FastAPI
import CoolProp.CoolProp as CP
import CoolProp.Plots as CPP
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/data/{FluidName}")
async def vL(FluidName: str):
    return {1/CP.PropsSI('D','P',1e5,'Q',0,FluidName)
}

