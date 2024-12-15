import org.junit.jupiter.api.Test;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class FindMaxTest {

    public static int findMax(int[] arr, int low, int high) {
        if (low == high) {
            return arr[low];
        }

        int mid = (low + high) / 2;
        int leftMax = findMax(arr, low, mid);
        int rightMax = findMax(arr, mid + 1, high);

        return Math.max(leftMax, rightMax);
    }

    @Test
    public void testFindMax() throws IOException {
        // Define the file path
        File file = new File("testdivide.txt");

        // Read the file
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line = br.readLine();

            // Parse the input from the file
            String[] parts = line.split("\\s{4}"); // Splits on 4 spaces
            int[] array = Arrays.stream(parts[0].replace("[", "").replace("]", "").split(","))
                                 .map(String::trim)
                                 .mapToInt(Integer::parseInt)
                                 .toArray();
            int expected = Integer.parseInt(parts[1].trim());

            // Assert the result
            assertEquals(expected, findMax(array, 0, array.length - 1));
        }
    }
}
