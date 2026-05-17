import java.util.*;

public class nqueen {

    // STEP 1: Check if it's safe to place a queen
    static boolean isSafe(int[][] board, int row, int col, int N) {
        
        // Check left side of current row
        for (int j = 0; j < col; j++) {
            if (board[row][j] == 1) return false;
        }

        // Check upper-left diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1) return false;
        }

        // Check lower-left diagonal
        for (int i = row, j = col; i < N && j >= 0; i++, j--) {
            if (board[i][j] == 1) return false;
        }

        return true; // Safe to place
    }

    // STEP 2: Place queens column by column using backtracking
    static boolean solve(int[][] board, int col, int N) {
        
        // All queens placed successfully
        if (col == N) return true;

        // Try placing queen in each row of current column
        for (int row = 0; row < N; row++) {
            if (isSafe(board, row, col, N)) {
                board[row][col] = 1;          // Place queen

                if (solve(board, col + 1, N)) // Recurse for next column
                    return true;

                board[row][col] = 0;          // Backtrack (remove queen)
            }
        }

        return false; // No valid position found
    }

    // STEP 3: Print the board
    static void printBoard(int[][] board, int N) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(board[i][j] == 1 ? " Q " : " _ ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter No of Queens: ");
        int N = sc.nextInt();

        int[][] board = new int[N][N]; // All cells = 0 by default

        if (solve(board, 0, N)) {
            System.out.println("\nSolution:");
            printBoard(board, N);
        } else {
            System.out.println("No solution exists for N = " + N);
        }

        sc.close();
    }
}