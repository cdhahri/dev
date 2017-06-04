package pack;

import java.io.File ;
import java.util.ArrayList;
import java.util.Random;

import weka.classifiers.Evaluation;
import weka.classifiers.evaluation.Prediction;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.trees.RandomForest;
import weka.core.converters.ConverterUtils.DataSource;
import weka.core.FastVector;
import weka.core.Instances;

public class WekaTest {

    public static void main(String[] args) throws Exception {
        Integer[] percentages = new Integer[]{10};
        for (Integer percentage : percentages) {
            File dir = new File("../output/weka");
            for (File file : dir.listFiles()) {
                DataSource source = new DataSource(file.getAbsolutePath());
                Instances data = source.getDataSet();
                data.setClassIndex(data.numAttributes() - 1);
                RandomForest rf = new RandomForest();
                Evaluation evaluation = new Evaluation(data);
                try {
                    evaluation.crossValidateModel(rf, data, 10, new Random(1));
                } catch(IllegalArgumentException ignored) {
                    continue;
                }
                System.out.println(file.getName());
                System.out.println(evaluation.toSummaryString());
/*
                ArrayList<Prediction> predictions = evaluation.predictions();
                String actual = String.format("%f", predictions.get(0).actual());
                String predicted = String.format("%f", predictions.get(0).predicted());
                for (int i = 1; i < predictions.size(); i++) {
                actual = String.format("%s, %f", actual, predictions.get(i).actual());
                predicted = String.format("%s, %f", predicted, predictions.get(i).predicted());
                }
                System.out.println(String.format("\"%s\":{\"actual\":[%s],\"predicted\":[%s]},",file.getName(), actual, predicted));
*/
            }
        }
    }
}
