% Generate random data, encode with a Convolutional code, propagate over
% BSC and get corresponding received data

BSCErrorProb = 0.03; % Error probability for the Binary symmetric channel
frameLength = 300;
data = randi([0 1],frameLength,1);
hConEnc = comm.ConvolutionalEncoder('TrellisStructure',poly2trellis(7, [171 133]),'TerminationMethod','Truncated');
hChan = comm.BinarySymmetricChannel('ErrorProbability',BSCErrorProb);
encodedData = step(hConEnc, data);
[receivedData, err]  = step(hChan, encodedData);
%stem([encodedData receivedData err]);
stem(err); 
errorloc = find(err)

