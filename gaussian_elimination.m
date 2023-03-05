function [R] = gaussian_elimination(A)
%GAUSSIAN_ELIMINATION  Returns Row Reduced Echelon Form of a matrix A.
%
%   Input:
%       A - Input Matrix. Should be a Matrix with valid values.
%
%   Output:
%       R - Row Reduced Echelon Form of A. Matrix with same dimension of A.

%   Base Case R and starting with row 1 and column 1.
    R = A;
    i=1; 
    j=1;
    [m,n] = size(R);

%   Operating on the new matrix
    while i<=m && j<=n
%       Finding Row with the largest absolute jth element.
        k = i;
        km = abs(R(i,j));
        for a = i:m
            if abs(R(a,j)) > km
                k = a;
                km = abs(R(a,j));
            end
        end

%       Swapping row i and k
        for b = 1:n
            temp = R(i,b);
            R(i,b) = R(k,b);
            R(k,b) = temp;
        end

%       Row Reduced Echelon Form Operations.        
        if km>10^-16
            a = R(i,j);
            for k = j:n
                R(i,k) = R(i,k)/a;
            end
            for k = [1:i-1, i+1:m]
                a = R(k,j);
                for l = j:n
                    R(k,l) = R(k,l) - a * R(i,l);
                end
            end
            i = i+1;
            j = j+1;
        else
            j = j+1;
        end
    end

end % umathur_pp6

