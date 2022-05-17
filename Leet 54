class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
       int m = matrix.length, n = matrix[0].length;
       //System.out.println(m); 
       List<Integer> ans = new ArrayList<Integer>();
       int block [][] = new int [m][n]; 
       Integer i=0, j=0, turn = 0; 
       while(ans.size() != matrix.length * matrix[0].length){
          if(turn % 4 == 0){
             while( turn/4 + j < n){
                ans.add(matrix[i][j]);
                ++j; 
             }
             --j;
             ++i; 
             ++turn; 
          }
          else if(turn % 4 == 1){
             while( turn/4 + i < m){
                ans.add(matrix[i][j]);
                ++i; 
             }
             --i;
             --j; 
             ++turn; 
          }
          else if(turn % 4 == 2){
             while( j >= turn/4){
                ans.add(matrix[i][j]);
                --j; 
             }
             ++j;
             --i; 
             ++turn; 
          }
          else {
             while( i >= (turn+1)/4){
                ans.add(matrix[i][j]);
                --i; 
             }
             ++i;
             ++j; 
             ++turn; 
          }    
       }
       return ans; 
    }
}
