import Hookworm_ParameterClasses as P
import Hookworm_MarkovModel as MarkovCls
import scr.FigureSupport as Figs

# create and cohort
cohort = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.SEMI)

simOutputs = cohort.simulate()


# graph histogram of infection durations
Figs.graph_histogram(
    data=simOutputs.get_infection_durations(),
    title='Cumulative Infection Duration under Semi-Annual MDA',
    x_label='Infection Duration (years)',
    y_label='Frequency',
    bin_width=1
)

# graph histogram of number of infections
Figs.graph_histogram(
    data=simOutputs.get_if_developed_infection(),
    title='Number of Infections per Patient Under Semi-Annual MDA',
    x_label='Number of Infections',
    y_label='Frequency',
    bin_width=1
)

Figs.graph_histogram(
    data=simOutputs.get_if_treated(),
    title='Number of Times Treated with Albendazole Under Semi-Annual MDA',
    x_label = 'Number of Treatments',
    y_label="Frequency",
    bin_width = 1
)
