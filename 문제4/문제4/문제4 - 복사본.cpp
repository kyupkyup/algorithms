#define _CUR_SECURE_NO_WARNINGS

#include<iostream>
#include<algorithm>
#include<vector>
#include<string.h>
#include<sstream>

using namespace std;


// cpp : 0  java 1 , python 2
// ba : 0 front 1
// juno : 0 sen 1
//chick : 0 pizza 1
//score 1~100000
// - is -1
int main()
{

   vector<string> info_not_spilit = { "java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50" };
   vector<string> qeury_not_spilit = { "java and - and - and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150" };

   
   vector<vector<string>> tokens_info_vector;
   vector<vector<string>> tokens_query_vector;

   for (int i = 0; i < info_not_spilit.size(); i++)
   {
      string buf;
      stringstream ss(info_not_spilit[i]);
      vector<string> token;
      while (ss >> buf)
         token.push_back(buf);

      tokens_info_vector.push_back(token);
   }

   for (int i = 0; i < qeury_not_spilit.size(); i++)
   {
      string buf;
      stringstream ss(qeury_not_spilit[i]);
      vector<string> token;
      while (ss >> buf)
      {
         if((buf=="and") == false)
            token.push_back(buf);
      }

      tokens_query_vector.push_back(token);
   }


   for (int i = 0; i < tokens_query_vector.size(); i++)
   {
      vector<string> query = tokens_query_vector[i];
      vector<vector<string>> cod;

      for (int i = 0; i < tokens_info_vector.size(); i++)
      {
         vector<string> temp;
         for (int j = 0; j < tokens_info_vector[i].size(); j++)
         {
            temp.push_back(tokens_info_vector[i][j]);
         }
         cod.push_back(temp);
      }

      int front = 0;
      int end = 5; // arr_size end
      int this_condition = 0;
      bool front_find = false;
      bool end_find = false;
      int result = 0;


      for (int i = 0; i < query.size(); i++)
      {
         if (query[i] == "-")
         {
            query.erase(query.begin() + i);
            for (int j = 0; j < cod.size(); j++)
            {
               //v.erase(v.begin()+4)
               cod[j].erase(cod[j].begin() + i);
            }
            i--;
         }
      }

      sort(cod.begin(), cod.end());

      while (this_condition < query.size())
      {
         if (front > end)
         {
            result = -1;
            break;
         }

         if (this_condition != query.size() - 1)
         {
            //마지막 컨디션 전까지는 
            if (cod[front][this_condition] == query[this_condition])
               front_find = true;
            else
               front++;

            if (cod[end][this_condition] == query[this_condition])
               end_find = true;
            else
               end--;
         }
         else
         {
            if (cod[front][this_condition] >= query[this_condition])
               front_find = true;
            else
               front++;

            if (cod[end][this_condition] >= query[this_condition])
               end_find = true;
            else
               end--;
         }


         if (front_find == true && end_find == true)
         {
            front_find = false;
            end_find = false;
            this_condition++;
         }
      }
      if (result == -1)
         cout << 0;
      else
         cout << end - front + 1;
   }


   
}