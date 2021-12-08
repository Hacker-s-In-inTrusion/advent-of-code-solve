#include <bits/stdc++.h>

using namespace std;

vector<string> seg_i, seg_o;
vector<string> seg_num(10);
int ans = 0;

int get_common(string a, string b)
{
  int cnt = 0;
  int len1 = a.length();
  int len2 = b.length();

  for (int i = 0; i < len1; i++)
  {
    for (int j = 0; j < len2; j++)
    {
      if (a[i] == b[j])
      {
        cnt++;
        break;
      }
    }
  }
  return cnt;
}

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

  for (int i = 0; i < sz / 4; i++)
  {
    for (int j = i * 10; j < (i + 1) * 10; j++)
    {
      if (seg_i[j].length() == 2)
      {
        sort(seg_i[j].begin(), seg_i[j].end());
        seg_num[1] = seg_i[j];
      }

      else if (seg_i[j].length() == 3)
      {
        sort(seg_i[j].begin(), seg_i[j].end());
        seg_num[7]= seg_i[j];
      }

      else if (seg_i[j].length() == 4)
      {
        sort(seg_i[j].begin(), seg_i[j].end());
        seg_num[4]= seg_i[j];
      }

      else if (seg_i[j].length() == 7)
      {
        sort(seg_i[j].begin(), seg_i[j].end());
        seg_num[8]= seg_i[j];
      }
    }

    for (int j = i * 10; j < (i + 1) * 10; j++)
    {
      if (seg_i[j].length() == 5)
      {
        if (get_common(seg_i[j], seg_num[4]) == 2)
        {
          sort(seg_i[j].begin(), seg_i[j].end());
          seg_num[2] = seg_i[j];
        }
      }
    }

    for (int j = i * 10; j < (i + 1) * 10; j++)
    {
      if (seg_i[j].length() == 5)
      {
        if (get_common(seg_i[j], seg_num[2]) == 3)
        {
          sort(seg_i[j].begin(), seg_i[j].end());
          seg_num[5] = seg_i[j];
        }

        else if (get_common(seg_i[j], seg_num[2]) == 4)
        {
          sort(seg_i[j].begin(), seg_i[j].end());
          seg_num[3] = seg_i[j];
        }
      }
    }

    for (int j = i * 10; j < (i + 1) * 10; j++)
    {
      if (seg_i[j].length() == 6)
      {
        if (get_common(seg_i[j], seg_num[3]) == 5)
        {
          sort(seg_i[j].begin(), seg_i[j].end());
          seg_num[9] = seg_i[j];
        }

        else if (get_common(seg_i[j], seg_num[1]) == 2)
        {
          sort(seg_i[j].begin(), seg_i[j].end());
          seg_num[0] = seg_i[j];
        }

        else
        {
          sort(seg_i[j].begin(), seg_i[j].end());
          seg_num[6] = seg_i[j];
        }
      }
    }

    int tmp = 0;

    for (int j = i * 4; j < (i + 1) * 4; j++)
    {
      sort(seg_o[j].begin(), seg_o[j].end());

      for (int k = 0; k < 10; k++)
      {
        if(!seg_num[k].compare(seg_o[j]))
        {
          tmp = tmp * 10 + k;
          break;
        }
      }
    }

    ans += tmp;
  }

  cout << ans;

  return 0;
}