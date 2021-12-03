#include <bits/stdc++.h>

using namespace std;

vector<string> report;
string gamma_rate = "";
string eplison_rate = "";

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  while (!cin.eof() && cin.good())
  {
    string s;
    cin >> s;
    report.push_back(s);
  }

  int sz = report.size();
  int len = report[0].length();

  for (int i = 0; i < len; i++)
  {
    int zc = 0, fc = 0;

    for (int j = 0; j < sz; j++)
    {
      if (report[j][i] == '0')
        zc++;

      else if (report[j][i] == '1')
        fc++;
    }

    if (zc > fc)
    {
      gamma_rate += "0";
      eplison_rate += "1";
    }

    else
    {
      gamma_rate += "1";
      eplison_rate += "0";
    }
  }

  bitset<12> g(gamma_rate);
  bitset<12> e(eplison_rate);

  unsigned long long cg = g.to_ullong();
  unsigned long long ce = e.to_ullong();

  cout << cg * ce;

  return 0;
}