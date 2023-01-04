import mesa

from Model import ExhaustModel


def agent_portrayal(agent):
    if agent is None:
        return

    portrayal = {"Shape": "circle", "Filled": "true", "Layer": 0}
    (x,y) = agent.pos
    portrayal['x'] = x
    portrayal['y'] = y
    if agent.accumulation_size == 1: #standard exhaust portrayal
        portrayal["Color"] = '#A0A0A0' #light gray
        portrayal['r'] = 0.2 #small size

    elif agent.accumulation_size == 2: #one accumulation point
        portrayal["Color"] = '#606060'  # medium gray
        portrayal['r'] = 0.4  # normal size

    elif agent.accumulation_size == 3: #two accumulation points
        portrayal["Color"] = '#202020'  # dark gray
        portrayal['r'] = 0.6  # large size

    elif agent.accumulation_size >= 4: #three or more accumulation points
        portrayal["Color"] = '#000000'  # black
        portrayal['r'] = 1  # very large size
    return portrayal


grid = mesa.visualization.CanvasGrid(agent_portrayal, 100, 100, 1000, 1000)

model_params = {"height": 100,
                "width": 100,
                "exhaust_prob": mesa.visualization.Slider("Exhaust Probability", 0.6,0.01, 1, 0.01)
                }
server = mesa.visualization.ModularServer(ExhaustModel, [grid], "Exhaust_Model", model_params)


server.port = 8521 #default port
server.launch()
