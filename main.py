from utils import START,END,ADD,MULT,DIV,move_direct,is_even,is_odd
from processes.process import Process
from processes.additon import ProcessAdd
from processes.multiplication import ProcessMult
from processes.division import ProcessDiv
from graph import Graph
from input import get_integer_list


numbers = get_integer_list()

graph = Graph(numbers)


graph.add_process(START, Process(START))
graph.add_process(END, Process(END))
graph.add_process(ADD, ProcessAdd(ADD))
graph.add_process(MULT, ProcessMult(MULT))
graph.add_process(DIV, ProcessDiv(DIV))


graph.add_edge(START, ADD, move_direct)  
graph.add_edge(ADD, ADD, is_odd)
graph.add_edge(ADD, MULT, is_even)
graph.add_edge(MULT, MULT, is_odd)
graph.add_edge(MULT, DIV, is_even)
graph.add_edge(DIV, END, move_direct)


graph.run(START)
