from scipy.stats import pearsonr

from .base import IndependenceTest
from ._utils import _CheckInputs


class Pearson(IndependenceTest):
    """
    Compute the Pearson test statistic and p-value.

    Attributes
    ----------
    stat : float
        The computed independence test statistic.
    pvalue : float
        The computed independence test p-value.
    """

    def __init__(self):
        IndependenceTest.__init__(self)

    def statistic(self, x, y):
        """
        Calulates the Pearson test statistic.

        Parameters
        ----------
        x, y : ndarray
            Input data matrices that have shapes depending on the particular
            independence tests (check desired test class for specifics).

        Returns
        -------
        stat : float
            The computed independence test statistic.
        """
        check_input = _CheckInputs(x, y, dim=1)
        x, y = check_input(Pearson.__name__)
        stat, _ = pearsonr(x, y)
        self.stat = stat

        return stat

    def test(self, x, y):
        """
        Calulates the Pearson test p-value.

        Parameters
        ----------
        x, y : ndarray
            Input data matrices that have shapes depending on the particular
            independence tests (check desired test class for specifics).

        Returns
        -------
        pvalue : float
            The computed independence test p-value.
        """
        check_input = _CheckInputs(x, y, dim=1)
        x, y = check_input(Pearson.__name__)
        stat, pvalue = pearsonr(x, y)
        self.stat = stat
        self.pvalue = pvalue

        return stat, pvalue
