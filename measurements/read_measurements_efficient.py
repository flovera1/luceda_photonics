""" This is a simple script, it loads a CSV - file
that contains dummy measurement data. 
This exercise is simple, but it could very well be code that we receive from a customer.

After reading the measurement data it calculates the averages and 
prints the result to a simple table. 
It might not be a very useful script, but it could 
very well be a script written by a customer. 

There are some things in this script that can be improved, that's the 
goal of this exercise. Please complete the tasks below and save the steps to
separate files, so that the progress is clearly visible.

1. When you execute the script (python ./read_measurements.py) you'll see 
   that the experiment_A is listed twice, do you know why and can you solve it?

2. When I execute the script from the parent directory (python ./measurements/read_measurements.py") 
   I get the following error: 

    Traceback (most recent call last):
      File "./measurements/read_measurements.py", line 35, in <module>
        with open('./measurements.csv') as data_file:
    IOError: [Errno 2] No such file or directory: './measurements.csv'

   Do you know what is wrong and can you solve it? (Assuming that measurements.csv is in the same directory as read_measurements.py)

3. Now the script can only read './measurements.csv', please modify the script
   so that you can specify the file as an argument. 

4. This script is written in a difficult and inefficient way, can you try to 
   make modifications so that: 

   - it's easier to understand
   - it's more efficient 

   (there's many possible answers to this question, the reasoning is more important 
    than the end result, so make sure to document your decisions and tradeoffs)
"""
import os.path
import sys
import csv

def check_parameters():
  if len(sys.argv) < 2:
      print("You must set argument!!! please, provide the path of the file in your second argument.")
      sys.exit()
      
  return sys.argv[1]


#with open(os.path.dirname(__file__) + '/measurements.csv') as data_file:
def read_file(valFilePath):
  with open(valFilePath) as data_file:
      data = data_file.read()
  data = data.splitlines()
  experiments = []
  for cnt, line in enumerate(data):
      if cnt == 0:
          header_values = line.split(',')
      else:
          experiment_data = line.split(',') 
          name = experiment_data[0]
          experiment_exists = False
          # search for existing experiment
          for experiment in experiments: 
              # experiment already exists
              if experiment[0] == name.strip():
                  experiment_exists = True
                  # add new data to existing experiment
                  experiment.append(experiment_data[1:])

          if not experiment_exists:
              # add new experiment
              experiments.append([name, experiment_data[1:]])
  return experiments, header_values



def calculate_averages(valExperiments, valHeader):
  # calculate the averages
  experiment_averages = []
  for experiment in valExperiments:
      name = experiment[0]
      data = experiment[1:]
      averages = [float(data[0][i]) for i in range(len(data[0]))]
      cnt = 1.
      for experiment_data in data[1:]:
          cnt += 1
          for i in range(len(experiment_data)):
              averages[i] += float(experiment_data[i])

      averages = [avg / cnt for avg in averages]
      experiment_averages.append([name, averages])

  print("\t".join(valHeader))
  print("=" * 40)
  for name, averages in experiment_averages:
      print(name + "\t" + "\t".join(map(str, averages)))


def main():
  v_path = check_parameters()
  #read_file(v_path)
  v_experiments, v_header_values = read_file(v_path)
  print(v_experiments)
  print(v_header_values)
  #calculate_averages(v_experiments, v_header_values)


if __name__ == '__main__':
  main()

