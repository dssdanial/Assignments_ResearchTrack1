% Danial Sabzevari     statistical analysis code
% Initialize and clear workspace
clc
clear 

% Set parameters
n_data = 9; 
random = false;

% Select paths based on the random flag
str_sol = getPath(random, "Solution", "distances from_gold_solution(");
str_my = getPath(random, "MY", "distances from_gold(");
my_str_time = getPath(random, "MY", "time(");
sol_str_time = getPath(random, "Solution", "time_solution(");

str = ").txt";
solutions_cell = cell(1, n_data + 1);
my_cell =  cell(1, n_data + 1);

% Import the data
[solutions_cell, my_cell] = importData(solutions_cell, my_cell, str_sol, str_my, n_data, str);

% Calculate statistics
my_std_array = calculateStdDev(my_cell, n_data);
sol_std_array = calculateStdDev(solutions_cell, n_data);
my_mean_array = calculateMean(my_cell, n_data);
sol_mean_array = calculateMean(solutions_cell, n_data);

% Calculate total mean
my_MEAN = mean(my_mean_array)';
sol_MEAN = mean(sol_mean_array)';

% Plot data
plotData(my_mean_array, my_MEAN, my_std_array, random, "my assignment");
plotData(sol_mean_array, sol_MEAN, sol_std_array, random, "prof solution");

% More code...
% ...

function path = getPath(random, dir, file)
    if (random == false)
        path = dir + "\" + file;
    else 
        path = dir + "_RANDOM\" + file;
    end
end

function [solutions_cell, my_cell] = importData(solutions_cell, my_cell, str_sol, str_my, n_data, str)
    for k = 0:n_data
        solutions_cell{k+1} = importdata(str_sol + num2str(k) + str); % Professor solution
        my_cell{k+1} = importdata(str_my + num2str(k) + str);         % My solution
    end
end

function std_array = calculateStdDev(cell_array, n_data)
    std_array = zeros(1, n_data);
    for k = 0:n_data
        std_array(k+1) = std(cell_array{k + 1});
    end
end

function mean_array = calculateMean(cell_array, n_data)
    mean_array = zeros(1, n_data);
    for k = 0:n_data
        mean_array(k+1) = mean(cell_array{k + 1});
    end
end

function plotData(mean_array, MEAN, std_array, random, title_modifier)
    figure
    y = [mean_array, MEAN];          
    errY = [std_array, 0];              
    h = barwitherr(errY, y);    
    if random == false
        title("Mean and Std Deviation from gold tokens, " + title_modifier + ", standardly placed silver tokens")
    else
        title("Mean and Std Deviation from gold tokens, " + title_modifier + ", randomly placed silver tokens")
    end
    set(gca,'XTickLabel',{'Run1','Run2','Run3', 'Run4', 'Run5', 'Run6', 'Run7','Run8', 'Run9', 'Run10', 'Total'},'fontweight','bold','fontsize',10);
    legend('Average Distance', 'Standard Deviation');
    ylabel('Average Distances from obastacles','fontweight','bold','fontsize',9);
    ylim([0 1.5])
    grid on
    set(h(1),'FaceColor', 'r');
end
