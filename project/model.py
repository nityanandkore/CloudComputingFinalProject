{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset = pd.read_csv('salary.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Index</th>\n",
       "      <th>experience</th>\n",
       "      <th>test_score</th>\n",
       "      <th>interview_score</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>zero</td>\n",
       "      <td>8.00000</td>\n",
       "      <td>9</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>zero</td>\n",
       "      <td>8.00000</td>\n",
       "      <td>6</td>\n",
       "      <td>45000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>five</td>\n",
       "      <td>6.00000</td>\n",
       "      <td>7</td>\n",
       "      <td>60000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>two</td>\n",
       "      <td>10.00000</td>\n",
       "      <td>10</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>seven</td>\n",
       "      <td>9.00000</td>\n",
       "      <td>6</td>\n",
       "      <td>70000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5</td>\n",
       "      <td>three</td>\n",
       "      <td>7.00000</td>\n",
       "      <td>10</td>\n",
       "      <td>62000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>6</td>\n",
       "      <td>ten</td>\n",
       "      <td>7.85714</td>\n",
       "      <td>7</td>\n",
       "      <td>72000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>7</td>\n",
       "      <td>eleven</td>\n",
       "      <td>7.00000</td>\n",
       "      <td>8</td>\n",
       "      <td>80000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Index experience  test_score  interview_score  salary\n",
       "0      0       zero     8.00000                9   50000\n",
       "1      1       zero     8.00000                6   45000\n",
       "2      2       five     6.00000                7   60000\n",
       "3      3        two    10.00000               10   65000\n",
       "4      4      seven     9.00000                6   70000\n",
       "5      5      three     7.00000               10   62000\n",
       "6      6        ten     7.85714                7   72000\n",
       "7      7     eleven     7.00000                8   80000"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['experience'].fillna(0, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = dataset.iloc[:, :3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Converting words to integer values\n",
    "def convert_to_int(word):\n",
    "    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,\n",
    "                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}\n",
    "    return word_dict[word]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     0\n",
       "1     0\n",
       "2     5\n",
       "3     2\n",
       "4     7\n",
       "5     3\n",
       "6    10\n",
       "7    11\n",
       "Name: experience, dtype: int64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X['experience']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = dataset.iloc[:, -1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Splitting Training and Test Set\n",
    "#Since we have a very small dataset, we will train our model with all availabe data.\n",
    "\n",
    "from sklearn.linear_model import LinearRegression\n",
    "regressor = LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Fitting model with trainig data\n",
    "regressor.fit(X, y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Saving model to disk\n",
    "pickle.dump(regressor, open('model.pkl','wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[77101.29500127]\n"
     ]
    }
   ],
   "source": [
    "# Loading model to compare the results\n",
    "model = pickle.load(open('model.pkl','rb'))\n",
    "print(model.predict([[9, 9, 6]]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
