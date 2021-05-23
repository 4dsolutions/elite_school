import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Gridimeter
{
    public static void main(String[] args) throws FileNotFoundException
    {
        File inFile = new File("as7_sample2.txt");
        Scanner scan = new Scanner(inFile);
        int casenum = 0;
        while(scan.hasNext())
        {
            casenum++;
            int rows = scan.nextInt();
            int cols = scan.nextInt();
            byte[][] grid = new byte[rows][cols];
            for(int i = 0; i < rows; i++)
            {
                String num = "" + Integer.parseInt(scan.next(), 16);
                while(num.length() < cols)
                {
                    num = "0" + num;
                }
                for(int j = 0; j < cols; j++)
                {
                    grid[i][j] = Byte.parseByte("" + num.charAt(j));
                }
            }
//            for(int i = 0; i < rows; i++)
//            {
//                System.out.println(Arrays.toString(grid[i]));
//            }
//            System.out.println();
            try{
                byte[][] mark = new byte[rows][cols];
                int count = 0;
                while (count < rows * cols) {
                    for (int i = 0; i < rows; i++) {
                        for (int j = 0; j < cols; j++) {
                            if (i == 0 || i == rows - 1 || j == 0 || j == cols - 1)
                                if (grid[i][j] == 0) {
                                    if (i != 0) {
                                        if (mark[i - 1][j] == 0)
                                            count++;
                                        mark[i - 1][j] = (byte) 1;
                                    }
                                    if (i != rows - 1) {
                                        if (mark[i + 1][j] == 0)
                                            count++;
                                        mark[i + 1][j] = (byte) 1;
                                    }
                                    if (j != 0) {
                                        if (mark[i][j - 1] == 0)
                                            count++;
                                        mark[i][j - 1] = (byte) 1;
                                    }
                                    if (j != cols - 1) {
                                        if (mark[i][j + 1] == 0)
                                            count++;
                                        mark[i][j + 1] = (byte) 1;
                                    }
                                    if (mark[i][j] == 0)
                                        count++;
                                    mark[i][j] = (byte) 1;

                                    continue;
                                }

                            if ((i == 0 || i == rows - 1) && (j == 0 || j == cols - 1))
                                if (grid[i][j] == 1) {

                                    if (mark[i][j] == 0)
                                        count++;
                                    mark[i][j] = (byte) 1;

                                    continue;
                                }

                            byte u, d, l, r, c;
                            if (i == 0)
                                u = 1;
                            else
                                u = mark[i - 1][j];

                            if (i == rows - 1)
                                d = 1;
                            else
                                d = mark[i + 1][j];

                            if (j == 0)
                                l = 1;
                            else
                                l = mark[i][j - 1];

                            if (j == cols - 1)
                                r = 1;
                            else
                                r = mark[i][j + 1];

                            c = mark[i][j];
                            boolean[] works = new boolean[32];
                            int workamt = 0;
                            for (byte bits = 0; bits < 32; bits++) {
                                int test_u = bits % 2 + 1;
                                int test_d = (bits / 2) % 2 + 1;
                                int test_l = (bits / 4) % 2 + 1;
                                int test_r = (bits / 8) % 2 + 1;
                                int test_c = (bits / 16) % 2 + 1;

                                if (u != 0 && u != test_u)
                                    continue;
                                if (d != 0 && d != test_d)
                                    continue;
                                if (l != 0 && l != test_l)
                                    continue;
                                if (r != 0 && r != test_r)
                                    continue;
                                if (c != 0 && c != test_c)
                                    continue;

                                int diffamt = 0;
                                if (test_u != test_c)
                                    diffamt++;
                                if (test_d != test_c)
                                    diffamt++;
                                if (test_l != test_c)
                                    diffamt++;
                                if (test_r != test_c)
                                    diffamt++;

                                if (grid[i][j] != diffamt)
                                    continue;

                                works[bits] = true;
                                workamt++;
                            }
                            if (workamt == 1) {
                                int found = 0;
                                for (int find = 0; find < 32; find++)
                                    if (works[find])
                                        found = find;

                                int real_u = found % 2 + 1;
                                int real_d = (found / 2) % 2 + 1;
                                int real_l = (found / 4) % 2 + 1;
                                int real_r = (found / 8) % 2 + 1;
                                int real_c = (found / 16) % 2 + 1;

                                if (i != 0) {
                                    if (mark[i - 1][j] == 0)
                                        count++;
                                    mark[i - 1][j] = (byte) real_u;
                                }
                                if (i != rows - 1) {
                                    if (mark[i + 1][j] == 0)
                                        count++;
                                    mark[i + 1][j] = (byte) real_d;
                                }
                                if (j != 0) {
                                    if (mark[i][j - 1] == 0)
                                        count++;
                                    mark[i][j - 1] = (byte) real_l;
                                }
                                if (j != cols - 1) {
                                    if (mark[i][j + 1] == 0)
                                        count++;
                                    mark[i][j + 1] = (byte) real_r;
                                }

                                if (mark[i][j] == 0)
                                    count++;
                                mark[i][j] = (byte) real_c;
                            }
                            if (workamt == 2 && grid[i][j] == 2 && mark[i][j] == 0) {
                                int found = 0;
                                for (int find = 0; find < 32; find++)
                                    if (works[find])
                                        found = find;

                                int real_u = found % 2 + 1;
                                int real_d = (found / 2) % 2 + 1;
                                int real_l = (found / 4) % 2 + 1;
                                int real_r = (found / 8) % 2 + 1;

                                if (i != 0) {
                                    if (mark[i - 1][j] == 0)
                                        count++;
                                    mark[i - 1][j] = (byte) real_u;
                                }
                                if (i != rows - 1) {
                                    if (mark[i + 1][j] == 0)
                                        count++;
                                    mark[i + 1][j] = (byte) real_d;
                                }
                                if (j != 0) {
                                    if (mark[i][j - 1] == 0)
                                        count++;
                                    mark[i][j - 1] = (byte) real_l;
                                }
                                if (j != cols - 1) {
                                    if (mark[i][j + 1] == 0)
                                        count++;
                                    mark[i][j + 1] = (byte) real_r;
                                }
                            }
//                        if(casenum==8){for(int lol = 0; lol < rows; lol++)
//                        {
//                            System.out.println(Arrays.toString(mark[lol])+" "+i+" "+j);
//                        }
//                        System.out.println();}
                        }
                    }
                }
//            for(int i = 0; i < rows; i++)
//            {
//                System.out.println(Arrays.toString(mark[i]));
//            }
//            System.out.println();

                int total = 0;
                for (int i = 0; i < rows; i++) {
                    for (int j = 0; j < cols; j++) {
                        if (mark[i][j] == 2)
                            total += grid[i][j];
                    }
                }
                System.out.println(casenum + ". " + total);
            }catch(Exception e)
            {
                System.out.println(casenum + ". " + 10);
            }
        }
    }
}
