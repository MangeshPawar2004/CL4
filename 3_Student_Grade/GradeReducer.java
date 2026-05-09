import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class GradeReducer extends Reducer<Text, IntWritable, Text, Text> {

    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {

        int total = 0;

        for (IntWritable val : values) {
            total += val.get();
        }

        String grade;

        if (total >= 90)
            grade = "A";
        else if (total >= 80)
            grade = "B";
        else if (total >= 70)
            grade = "C";
        else if (total >= 60)
            grade = "D";
        else
            grade = "F";

        context.write(key, new Text(grade));
    }
}