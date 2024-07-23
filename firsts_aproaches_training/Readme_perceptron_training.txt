This is the first training of one Percetron i've done, i hope it result useful, here you can see all the adjustment it takes (only with 2 epochs) 
It's the classic binary training about the Iris dataset. It is a well-known dataset in the field of machine learning and statistics,
introduced by the British biologist and statistician Ronald A. Fisher in 1936.
The dataset contains measurements of iris flowers from three different species: Iris setosa, Iris versicolor, and Iris virginica.
The dataset includes features such as sepal length, sepal width, petal length, and petal width.

============================================================
                 Perceptron Training Overview
============================================================

1. **Initialization**:
   - **Weights**: `[0.2, -0.33, 0.05]`
   - **Learning Rate**: `0.01`
   - **Epochs**: `2`
   - **Activation Function**: Returns `1` if input > `0`, otherwise `-1`.

2. **Data**:
   - **Mapping**:
     - `'setosa'` → `1`
     - `'versicolor'` → `-1`
   - **Inputs**: `[1, sepal_length, petal_length]`
   - **Outputs**: Mapped class values.

3. **Training Process**:
   - For each epoch and data point:
     - **Compute Output**: Linear combination of weights and inputs.
     - **Apply Activation**: Use activation function on the linear output.
     - **Calculate Error**: Difference between actual and predicted output.
     - **Update Weights**: Adjust weights based on error and learning rate.
     - **Log Details**: Print data point, prediction, error, and updated weights.

4. **Results**:
   - Final weights are printed after training, showing the learned parameters.

============================================================
