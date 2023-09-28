from fastapi import FastAPI
import CoolProp.CoolProp as CP
import CoolProp.Plots as CPP

app = FastAPI()


@app.get("/PropsSI")
async def propssi(output_name: str, input_name1: str, input_prop1: float, input_name2: str, input_prop2: float,
                  fluid_name: str):
    return {CP.PropsSI(output_name, input_name1, input_prop1, input_name2, input_prop2, fluid_name)
            }


@app.get("/data/fluids")
async def fluidslist():
    return CP.FluidsList()


@app.get("/data/Output")
async def output_list():
    return {"Quality [-]": "Q", "Temperature [K]": "T", "Pressure [kPa]": "P", "Density [kg/m3]": "D",
            "Ideal-gas specific heat at constant pressure [kJ/kg/K]": "C0",
            "Specific heat at constant pressure [kJ/kg/K]": "C", "Specific heat at constant volume [kJ/kg/K]": "O",
            "Internal energy [kJ/kg]": "U", "Enthalpy [kJ/kg]": "H", "Entropy [kJ/kg/K]": "S",
            "Speed of sound [m/s]": "A", "Gibbs function [kJ/kg]": "G", "Dynamic viscosity [Pa-s]": "V",
            "Thermal conductivity [kW/m/K]": "L", "Surface Tension [N/m]": "I", "Accentric Factor [-]": "w"}


@app.get("/data/Input")
async def input_list():
    return {"T P",
            "T D",
            "P D",
            "T Q",
            "P Q",
            "H P",
            "S P",
            "S H",
            "T S"}
