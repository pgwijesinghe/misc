
lambda1 = 1064
lambda2 = 1535
method = 'dfg'
print(f'{1/(1/lambda1 + 1/lambda2)} nm') if method == 'sfg' else print(f'{1/abs((1/lambda1 - 1/lambda2))} nm') if method == 'dfg' else print('please select type: sfg or dfg')
