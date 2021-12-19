#include<iostream>
#include<vector>
#include<map>
#include<set>

using namespace std;

map<string, set<string>> g;
map<string, bool> visited;
int ans = 0;

vector<string> splitStringtoVector(const string& s)
{
  vector<string> result;
  size_t pos = 0, prev_pos = 0;
  string tmp;

  while ((pos = s.find('-', prev_pos)) != string::npos)
  {
    tmp = s.substr(prev_pos, pos - prev_pos);
    prev_pos = pos + 1;

    if (tmp.length() > 0)
      result.push_back(tmp);
  }

  tmp = s.substr(prev_pos);
  result.push_back(tmp);

  return result;
}

void dfs(string s)
{
  if (!s.compare("end"))
  {
    ans++;
    return;
  }

  for (auto e : g[s])
  {
    if (e[0] >= 'a' && e[0] <= 'z' && (e.compare("start") && e.compare("end")))
    {
      if (!visited[e])
      {
        visited[e] = true;
        dfs(e);
        visited[e] = false;
      }
    }

    else if (e.compare("start"))
      dfs(e);
  }
}

int main(void)
{
  while (!cin.eof() && cin.good())
  {
    string s;
    vector<string> tempVec;
    cin >> s;

    tempVec = splitStringtoVector(s);

    g[tempVec[0]].insert(tempVec[1]);
    g[tempVec[1]].insert(tempVec[0]);
  }

  for (auto it = g.begin(); it != g.end(); it++)
  {

    for (auto e : it->second)
    {
      if (e[0] >= 'a' && e[0] <= 'z' && (e.compare("start") && e.compare("end")))
        visited[e] = false;
    }
  }

  dfs("start");

  cout << ans;

  return 0;
}