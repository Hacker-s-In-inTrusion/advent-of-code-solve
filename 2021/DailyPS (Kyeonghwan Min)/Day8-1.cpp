#include <bits/stdc++.h>

using namespace std;

vector<string> seg_i, seg_o;
string seg_0 = "abcefg";
string seg_1 = "cf";
string seg_2 = "acdeg";
string seg_3 = "acdfg";
string seg_4 = "bcdf";
string seg_5 = "abdfg";
string seg_6 = "abdefg";
string seg_7 = "acf";
string seg_8 = "abcdefg";
string seg_9 = "abcdfg";

int ans = 0;

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  while (!cin.eof() && cin.good())
  {
    string s;

    for (int i = 0; i < 10; i++)
    {
      cin >> s;
      sort(s.begin(), s.end());
      seg_i.push_back(s);
    }

    cin >> s;

    for (int i = 0; i < 4; i++)
    {
      cin >> s;
      sort(s.begin(), s.end());
      seg_o.push_back(s);
    }
  }

  int sz = seg_o.size();

  for (int i = 0; i < sz; i++)
  {
    if (seg_o[i].length() == 2 || seg_o[i].length() == 3 || seg_o[i].length() == 4 || seg_o[i].length() == 7)
      ans++;
  }

  cout << ans;

  return 0;
}