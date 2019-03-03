#include "bits/stdc++.h"
using namespace std;

vector<int> root, p;
vector<vector<int> > g;

int _remove(int u) {
    if (g[u].size() == 0)
        return 1;
    else if (g[u].size() == 2) {
        int l = _remove(g[u][0]);
        int r = _remove(g[u][1]);
        if (abs(l - r) >= 2) {
            root.push_back(g[u][0]);
            root.push_back(g[u][1]);
            vector<int> &pred = g[p[u]];
            if (!pred.empty())
                pred.erase(find(pred.begin(), pred.end(), u));
            g[u].clear();
            return 0;
        } else {
            return 1 + l + r;
        }
    } else {
        int m = _remove(g[u][0]);
        if (m >= 2) {
            root.push_back(g[u][0]);
            vector<int> &pred = g[p[u]];
            if (!pred.empty())
                pred.erase(find(pred.begin(), pred.end(), u));
            g[u].clear();
            return 0;
        } else {
            return 1 + m;
        }
    }
}
void print_tree(int u) {
    if (g[u].size() == 0) {
        return;
    } else {
        for (auto e : g[u]) {
            cout << u << " => " << e << endl;
            print_tree(e);
        }
    }
}
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n, m;
    cin >> n >> m;
    g.resize(n + 1);
    p.resize(n + 1);
    int u, v;
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        g[u].push_back(v);
        p[v] = u;
    }
    int r;
    cin >> r;
    root.push_back(r);
    _remove(r);
    for (auto e : root) {
        if (g[e].size()) {
            print_tree(e);
            cout << endl;
        }
    }
    return 0;
}
