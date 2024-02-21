import asyncio
import logging
import json
from asyncua import Server, ua


async def main():
    # setup our server
    server = Server()
    await server.init()

    server.set_endpoint("opc.tcp://192.168.29.84:5001")

    # set up our own namespace, not really necessary but should as spec
    uri = "OPC UA SIMULATION SERVER"
    idx = await server.register_namespace(uri)
    sensor_data = await read_sensor_data('server/static/sensors.json')

    for sensor_name, sensor_entries in sensor_data.items():
        await set_sensor_data(sensor_name, sensor_entries, idx, server)

    print("server has started..........")

    async with server:
        while True:
            await asyncio.sleep(1)
    
async def read_sensor_data(filename):
    with open(filename, "r") as file:
        return json.load(file)
    
async def set_sensor_data(sensor_name, data, idx, server):
        # Add nodes for the sensor
        sensor_object = await server.nodes.objects.add_object(idx, sensor_name)

        for i, entry in enumerate(data):
            entry_name = f"{sensor_name}_{i}"  # Use index as unique identifier
            entry_object = await sensor_object.add_object(idx, entry_name)

            # Add variables for each attribute in the entry
            for key, value in entry.items():
                await entry_object.add_variable(idx, key, value)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)