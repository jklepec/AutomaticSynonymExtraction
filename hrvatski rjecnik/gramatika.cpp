#include <bits/stdc++.h>
using namespace std;
#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define REP(i, n) FOR(i, 0, n)
#define _ << " " <<
#define pb push_back

typedef double lf;
typedef long long ll;
typedef pair<int, int> pii;

// neka mjera za slicnost rijeci
const int CUT_OFF = 6;

int dp[100][100];


int levenstein(const string &x, const string &y) {
  int n = x.size() + 1;
  int m = y.size() + 1;

  for (int i = 0; i < max(n, m); i++) {
    dp[i][0] = dp[0][i] = i;
  }

  for (int i = 1; i < n; ++i) for (int j = 1; j < m; ++j) {
    int cost = 2;
    if (x[i] == y[j]) {
      cost = 0;
    }
    dp[i][j] = min(min(dp[i - 1][j] + 3, dp[i][j - 1] + 2), dp[i - 1][j - 1] + cost);

    if (i > 1 && j > 1 && x[i] == y[j - 1] && y[j] == x[i - 1]) {
      dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 2);
    }
  }

  return dp[n - 1][m - 1];
}

map<string, string> base; // nominativ rijeci
set<string> rijeci; // sve rijeci
map<string, vector<string>> graph;

map<string, int> indices; // index nominativa

vector<pair<int, int>> edges;

void dodaj(string x, string y) {
  int makni = max(0, min(2, (int) y.size() - 3));

  string y_lo = y.substr(0, y.size() - makni);
  string y_hi = y_lo;
  y_hi.back() += 1;

  vector<pair<int, string>> candidates;
  for (auto it = rijeci.lower_bound(y_lo); it != rijeci.end() && (*it) < y_hi; ++it) {
    candidates.push_back({levenstein(y, *it), *it});
  }

  sort(candidates.begin(), candidates.end());
  for (int i = 0; i < min((int) candidates.size(), 3); ++i) {
    if (candidates[i].first > CUT_OFF) break;
    edges.pb({indices[base[x]], indices[base[candidates[i].second]]});
  }
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(0);

  int n; cin >> n;

  REP(i, n) {
    int m; cin >> m;
    string x; cin >> x;
    // dodaj deklinacije

    indices[x] = i;
    base[x] = x;

    REP(j, m) {
      string y; cin >> y;
      //cout << m _ x _ y << endl;
      for (auto c: y) {
        //if (!((c >= 'a' && c <= 'z') || (c >= '0' && c <= '5'))) assert(false);
      }
      graph[x].pb(y);
    }

    rijeci.insert(x);
  }

  char last = 'b';
  for (auto x:rijeci) {
    if (x[0] != last) {
      last = x[0];
    }
    for (auto y:graph[x]) {
      dodaj(x, y);
    }
  }

  sort(edges.begin(), edges.end());
  for (auto e: edges) {
    if (e.first) cout << e.first _ e.second << endl;
  }
}
