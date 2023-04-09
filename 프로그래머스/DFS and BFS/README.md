# dfs/bfs

## 핵심

- 재귀 함수 사용해서 풀기 (global 사용 많이함
- DFS(깊이 우선 탐색)
    - 다음 분기로 넘어가기전 해당 분기를 완벽하게 탐색
    - **모든 노드 방문해야 할 때 사용**
    - 스택 or 재귀 함수 이용
    - [네트워크 문제](https://github.com/qpwisu/algorithm/blob/master/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/DFS%20and%20BFS/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC.py) (dfs)
        - 접촉한 곳을 2로 표시하고 접촉 안한곳은 재귀로  접근

  
- BFS(너비 우선 탐색)
    - 최대한 넓게 이동한 다음 더이상 갈 수 없을 때 아래로 이동
    - **최댄 경로를 찾고 싶을 때 사용**
    - Queue를 사용해서 접근 (collections의 deque)
    - 방문했는지 않했는지 list로 check
    - [단어 변환 문제](https://github.com/qpwisu/algorithm/blob/master/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/DFS%20and%20BFS/%EB%8B%A8%EC%96%B4%EB%B3%80%ED%99%98.py)
    - [게임 맵 최단 거리](https://github.com/qpwisu/algorithm/blob/master/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/DFS%20and%20BFS/%EA%B2%8C%EC%9E%84%EB%A7%B5%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC.py)
        - dx = [-1,1,0,0] , dy = [0,0,-1,1] 로 for문 돌면서 동서남북 접근하는데 visited에 이미 방문했으면 넘어감