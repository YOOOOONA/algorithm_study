//파이썬으로는 시간초과를 피할수 없는문제
//(진짜 최적화를 잘 시킨다면 가능이야하겠지만 그만큼의 알고리즘을 요구하는게 아닌 문제)
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
using pr = pair<int, int>;

int board[11][11];
int ans = 0;
int N, M, H;
int milk_cnt;
pr start;

void dfs(vector<pr> milk, pr now, int M) {
   vector<pr> mk;
   pr m;
   
   int move,nM;
   for (int i = 0; i < milk.size(); i++) {
      mk.assign(milk.begin(), milk.end());//milk를 mk에 깊은 복사

      m = milk[i];
      move = abs(m.first - now.first) + abs(m.second - now.second);
      if (move <= M) {
         nM = M - move + H;
         if (nM >= 0) {
            auto it = remove(mk.begin(), mk.end(), m);
            mk.resize(it - mk.begin());
            dfs(mk, m, nM);
            if (m != start) {
               if (abs(start.first - m.first) + abs(start.second - m.second) <= nM) {//왜냐면 현재 now는 m임
                  ans = ans >= milk_cnt - mk.size() ? ans : milk_cnt - mk.size();
               }
            }
         }
      }
   }
}
int main() {
   ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
   //freopen(".\\input.txt", "r", stdin);
   cin >> N >> M >> H;
   vector<pr> MILK;
   for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
         cin >> board[i][j];
         if (board[i][j] == 1) {
            start.first = i;
            start.second = j;
         }
         else if (board[i][j] == 2) {
            MILK.push_back({ i,j });
         }
      }
   }
   milk_cnt = MILK.size();
   dfs(MILK, start, M);
   cout << ans;
}