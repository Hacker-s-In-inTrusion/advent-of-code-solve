#include <bits/stdc++.h>

using namespace std;

int ans = 0;
vector<long long int> score;

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  while (!cin.eof() && cin.good())
  {
    string s;
    cin >> s;

    stack<char> braket;

    int len = s.length();
    char illegal_braket = '0';

    if (len == 0)
      break;

    for (int i = 0; i < len; i++)
    {
      if (s[i] == '(' || s[i] == '[' || s[i] == '{' || s[i] == '<')
        braket.push(s[i]);

      else if (s[i] == ')')
      {
        if (!braket.empty())
        {
          if (braket.top() == '(')
            braket.pop();

          else
          {
            illegal_braket = s[i];
            break;
          }
        }
      }

      else if (s[i] == ']')
      {
        if (!braket.empty())
        {
          if (braket.top() == '[')
            braket.pop();

          else
          {
            illegal_braket = s[i];
            break;
          }
        }
      }

      else if (s[i] == '}')
      {
        if (!braket.empty())
        {
          if (braket.top() == '{')
            braket.pop();

          else
          {
            illegal_braket = s[i];
            break;
          }
        }
      }

      else if (s[i] == '>')
      {
        if (!braket.empty())
        {
          if (braket.top() == '<')
            braket.pop();

          else
          {
            illegal_braket = s[i];
            break;
          }
        }
      }
    }

    if (illegal_braket == '0')
    {
      long long int sum = 0;

      while (!braket.empty())
      {
        if (braket.top() == '(')
        {
          sum *= 5;
          sum += 1;
          braket.pop();
        }

        else if (braket.top() == '[')
        {
          sum *= 5;
          sum += 2;
          braket.pop();
        }

        else if (braket.top() == '{')
        {
          sum *= 5;
          sum += 3;
          braket.pop();
        }

        else if (braket.top() == '<')
        {
          sum *= 5;
          sum += 4;
          braket.pop();
        }
      }

      score.push_back(sum);
    }
  }

  sort(score.begin(), score.end());
  int sz = score.size();
  cout << score[sz / 2];

  return 0;
}