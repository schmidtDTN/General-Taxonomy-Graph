import networkx

fileLocation = 'FILEPATH GOES HERE'

capacities = ["Language", "Spatial", "Reasoning", "Decision-Making", "Categorization", "Perceptual", "Memory", "Motor",
              "Learning", "Attention", "Emotion"]

# Activity, Attribute, Direction, Entity Resolution, Location, Material, Reasoning, Sentiment, Size, State, Numerosity
taxo_gaps = [{"Lexical": ["Language", "Reasoning", "Decision-Making"]},
             {"Word-Sense": ["Language", "Reasoning"]},
             {"Negation": ["Language", "Reasoning"]},
             {"Part-Of-Speech": ["Language"]},
             {"Sentiment": ["Language", "Memory", "Attention", "Emotion"]},
             {"Target": ["Language", "Reasoning", "Perceptual"]},
             {"Context": ["Spatial", "Perceptual", "Memory", "Attention"]},
             {"Direction": ["Spatial", "Perceptual", "Attention"]},
             {"Size": ["Spatial", "Perceptual", "Attention"]},
             {"Numerosity": ["Reasoning", "Perceptual", "Attention"]},
             {"Replication": ["Memory", "Motor", "Learning"]},
             {"Cue": ["Decision-Making", "Categorization", "Attention"]},
             {"Boundary": ["Reasoning", "Decision-Making", "Perceptual", "Motor", "Learning"]},
             {"Explanatory": ["Reasoning", "Categorization", "Memory", "Learning"]},
             {"Update": ["Memory", "Attention"]},
             {"Memory": ["Memory", "Attention"]},
             {"Metonymy": ["Language", "Reasoning", "Categorization"]},
             {"Rationality": ["Reasoning", "Categorization", "Memory", "Emotion"]},
             {"Ignorance": ["Reasoning", "Decision-Making", "Memory"]},
             {"Procedural": ["Memory", "Motor", "Learning", "Attention"]}]

vqa_gaps = [{"Activity": ["Reasoning", "Categorization", "Perceptual"]},
            {"Attribute": ["Categorization", "Perceptual"]},
            {"Direction": ["Spatial", "Perceptual", "Attention"]},
            {"Entity Resolution": ["Reasoning"]},
            {"Location": ["Spatial", "Perceptual", "Attention"]},
            {"Material": ["Categorization", "Perceptual"]},
            {"Reasoning": ["Reasoning", "Memory", "Learning"]},
            {"Sentiment": ["Language", "Memory", "Attention", "Emotion"]},
            {"Size": ["Spatial", "Perceptual", "Attention"]},
            {"State": ["Reasoning", "Categorization", "Perceptual"]},
            {"Numerosity": ["Reasoning", "Perceptual", "Attention"]}]

graph = networkx.Graph()
graph.add_nodes_from(capacities)

for gapType in vqa_gaps:
    # Go through each gap type
    for gapTypeName in gapType:
        # Get the list of capabilities associated with it
        gapCapabilityList = gapType.get(gapTypeName)
        print(gapTypeName)
        print(gapCapabilityList)
        # Create a node for the gap type
        gapTypeName = gapTypeName
        graph.add_node(gapTypeName)
        # Iterate through the capabilities and connect each one to the gap type via an edge
        for capability in gapCapabilityList:
            graph.add_edge(gapTypeName, capability, label="affects")

networkx.write_graphml_lxml(graph, fileLocation)
