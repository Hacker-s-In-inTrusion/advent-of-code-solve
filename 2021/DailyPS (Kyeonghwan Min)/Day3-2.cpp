#include <bits/stdc++.h>

using namespace std;

vector<string> report;
string gamma_rate = "";
string eplison_rate = "";

unsigned long long get_ogr(void)
{
  vector<string> tmp1, tmp2;

  tmp1 = report;
  int idx = 0;

  while (tmp1.size() > 1)
  {
    int sz = tmp1.size();
    int fc = 0, zc = 0;

    for (int i = 0; i < sz; i++)
    {
      if (tmp1[i][idx] == '0')
        zc++;

      else if (tmp1[i][idx] == '1')
        fc++;
    }

    if (fc >= zc)
    {
      for (int i = 0; i < sz; i++)
      {
        if (tmp1[i][idx] == '1')
          tmp2.push_back(tmp1[i]);
      }

      tmp1 = tmp2;
      tmp2.clear();
    }

    else
    {
      for (int i = 0; i < sz; i++)
      {
        if (tmp1[i][idx] == '0')
          tmp2.push_back(tmp1[i]);
      }

      tmp1 = tmp2;
      tmp2.clear();
    }

    idx++;
  }

  bitset<12> bogr(tmp1[0]);

  return bogr.to_ullong();
}

unsigned long long get_csr(void)
{
  vector<string> tmp1, tmp2;

  tmp1 = report;
  int idx = 0;

  while (tmp1.size() > 1)
  {
    int sz = tmp1.size();
    int fc = 0, zc = 0;

    for (int i = 0; i < sz; i++)
    {
      if (tmp1[i][idx] == '0')
        zc++;

      else if (tmp1[i][idx] == '1')
        fc++;
    }

    if (fc < zc)
    {
      for (int i = 0; i < sz; i++)
      {
        if (tmp1[i][idx] == '1')
          tmp2.push_back(tmp1[i]);
      }

      tmp1 = tmp2;
      tmp2.clear();
    }

    else
    {
      for (int i = 0; i < sz; i++)
      {
        if (tmp1[i][idx] == '0')
          tmp2.push_back(tmp1[i]);
      }

      tmp1 = tmp2;
      tmp2.clear();
    }

    idx++;
  }

  bitset<12> bcsr(tmp1[0]);

  return bcsr.to_ullong();
}

int main(void)
{
  //cin.tie(NULL);
  //ios::sync_with_stdio(false);

  while (!cin.eof() && cin.good())
  {
    string s;
    cin >> s;
    report.push_back(s);
  }

  unsigned long long ogr = get_ogr();
  unsigned long long cgr = get_csr();

  cout << ogr * cgr;

  return 0;
}