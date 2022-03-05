class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        int num = connections.size(); //number of connections
        if(n-1 > num) return -1;
        int iso = 0;
        vector<vector<int>> web (n);
        vector<int> flag (n);
        
        for(int i=0; i<n; ++i){
           flag[i] = i; 
        }
        
        bool change = true;
        while(change){
           change = false; 
           for(int i=0; i<num; ++i){
               int a = connections[i][0], b = connections[i][1];
               //web[a].push_back(b);
               //web[b].push_back(a);
               if(flag[b] > flag[a]){
                  flag[b] = flag[a];
                  change = true;
               }    
               else if(flag[b] < flag[a]){
                   flag[a] = flag[b];
                   change = true;
               }    
           }
        }
        
        
        //Orderness of connections is necessary: a>b so if flag[a] == -1, 
        //no Node value less than a is connected with a
        
        //nodes connected with a is greater than a from web
        //For the loop, make sure
        /*for(int i=0; i<n; ++i){
           //if(flag[i] == i){ 
              int min = flag[i];
              const int l = web[i].size(); 
              for(int j=0; j<l; ++j){
                 min = min > flag[j] ? flag[j] : min; 
              }
              flag[i] = min; 
              for(int j=0; j<l; ++j){
                    flag[web[i][j]] = min; 
                 }    
              //}
              for(int p=0; p<n; ++p){
                 cout << flag[p] << " "; 
              }
              printf("\n");    
        }*/   
        
        set<int> ans;  
        for(int i=0; i<n; ++i){
           ans.insert(flag[i]); 
        }
        return ans.size()-1;
    }
    
};


        /*
        vector<int> count (n,0);
        vector<vector<int>> web (n, vector<int>(n,1e5));
        for(int i=0; i<n; ++i){
           web[i][i] = 0; 
        }
        
        for(int i=0; i<num; ++i){
       
           int a = connections[i][0], b = connections[i][1]; 
           web[a][b] = 1;
           web[b][a] = 1;
           count[a]++;
           count[b]++;   
           //web[connections[i][1]].push_back(connections[i][0]);  
        }
        
       
        
        
        //Dijkstra
        bool change = true;
        int time = 0;
        
        while(change){
           ++time; 
           change = false; 
           for(int i=0; i<n; ++i){
               for(int j=i+1; j<n; ++j){
                  if(web[i][j] < 1e5){
                     for(int k=0; k<n; ++k){
                        if(web[i][j] + web[j][k] < web[i][k]){
                            web[i][k] = web[i][j] + web[j][k]; 
                            web[k][i] = web[i][k];
                            change = true;
                        }    
                     } 
                  }   
               }
           }
        }
        //cout << "time = " << time << "\n";
        
        for(int i=0; i<n; ++i){
            for(int j=0; j<n; ++j){
               cout << web[i][j] << " "; 
            }
            cout << "\n";
        }
        
        //check connected local pattern and edge
        vector<bool> vis (n,false);
        int iso = 0;
        for(int i=0; i<n; ++i){
           if(vis[i]) continue;
           else if(count[i] == 0){
               ++iso;
               continue;
           } 
           int v = 1;
           int e = count[i]; 
           for(int j=i+1; j<n; ++j){
              if(!vis[j] && web[i][j] < 1e5){
                  ++v;
                  e += count[j];
                  vis[j] = true;
                  
              }  
           }
           e /= 2; 
           ++iso;
        }
        */
