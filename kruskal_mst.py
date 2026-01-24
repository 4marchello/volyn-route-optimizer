{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "28ea6231-a1e5-4a2f-8cf3-d02652170af9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def kruskal():\n",
    "    num_of_ver = int(input(\"Enter the number of vertex: \"))\n",
    "    num_of_eg = int(input(\"Enter the number of edges: \"))\n",
    "    edges = []\n",
    "    print(\"Enter (weight vertex1 vertex2):\")\n",
    "    for _ in range(num_of_eg):\n",
    "        data = input().split()\n",
    "        edges.append((float(data[0]), data[1], data[2]))\n",
    "    sorted_edges = sorted(edges, key = lambda x: x[0])\n",
    "    \n",
    "    connections = {}\n",
    "\n",
    "    def get_root(vertex):\n",
    "        if vertex not in connections: \n",
    "            connections[vertex] = vertex\n",
    "        if connections[vertex] == vertex: \n",
    "            return vertex\n",
    "        connections[vertex] = get_root(connections[vertex])\n",
    "        return connections[vertex]\n",
    "\n",
    "    def join_sets(a, b):\n",
    "        root_a, root_b = get_root(a), get_root(b)\n",
    "        if root_a != root_b:\n",
    "            connections[root_a] = root_b\n",
    "            return True\n",
    "        return False\n",
    "\n",
    "    def join_groups(vertex_a, vertex_b):\n",
    "        head_a = get_root(vertex_a)\n",
    "        head_b = get_root(vertex_b)\n",
    "        if head_a != head_b:\n",
    "            connections[head_a] = head_b\n",
    "            return True\n",
    "        return False\n",
    "    mst = []\n",
    "    total_weight = 0\n",
    "\n",
    "    for w, v1, v2 in sorted_edges:\n",
    "        if join_sets(v1, v2):\n",
    "            mst.append((v1, v2, w))\n",
    "            total_weight += w\n",
    "            if len(mst) == num_of_ver - 1:\n",
    "                break\n",
    "\n",
    "    print(\"\\nMST:\")\n",
    "    for v1, v2, w in mst:\n",
    "        print(f\"{v1} - {v2}\")\n",
    "    print(f\"Total distance: {total_weight}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f17bed5b-4589-458c-a774-ed67dd32aff5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Введіть кількість вершин:  7\n",
      "Введіть кількість ребер:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введіть (вага вершина1 вершина2):\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 61.8 1 3\n",
      " 60.6 1 5 \n",
      " 59 2 3 \n",
      " 32 2 6\n",
      " 52 2 7\n",
      " 66 3 4 \n",
      " 93 3 6\n",
      " 60 3 7\n",
      " 151.1 4 5\n",
      " 77 4 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "MST:\n",
      "2 - 6\n",
      "2 - 7\n",
      "2 - 3\n",
      "1 - 5\n",
      "1 - 3\n",
      "3 - 4\n",
      "Загальна вага: 331.4\n"
     ]
    }
   ],
   "source": [
    "kruskal()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00fcdec5-36c5-412c-b1f3-833e84402938",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
