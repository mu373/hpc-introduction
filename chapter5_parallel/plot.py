import argparse
import glob
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


def read_all_results(input_dir: str) -> pd.DataFrame:
    """
    Read all per-p CSVs from the input directory and concatenate into one DataFrame.

    Parameters
    ----------
    input_dir : str
        The directory containing the input CSV files.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing all the concatenated results.
    """
    files = sorted(glob.glob(os.path.join(input_dir, "p_*.csv")))
    if not files:
        print(f"No CSV files found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    dfs = []
    for f in files:
        df = pd.read_csv(f)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)


def aggregate_by_p(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by p and compute mean & std for clustering and degree.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame containing all simulation results.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the aggregated results.
    """
    g = df.groupby("p", as_index=False).agg(
        n=("trial_id", "count"),
        degree_mean=("avg_degree", "mean"),
        degree_std=("avg_degree", "std"),
    )
    g[["degree_std"]] = g[["degree_std"]].fillna(0.0)
    return g.sort_values("p")


def plot_avg_degree(summary: pd.DataFrame, out_path: str) -> None:
    """
    Plot p vs average degree with error bars and theory line.

    Parameters
    ----------
    summary : pd.DataFrame
        The input DataFrame containing aggregated simulation results.
    out_path : str
        The output file path for the plot.

    Returns
    -------
    None
    """
    p = summary["p"].values
    y = summary["degree_mean"].values
    yerr = summary["degree_std"].values

    fig, ax = plt.subplots(1, 1, figsize=(4, 3))
    ax.errorbar(p, y, yerr=yerr, fmt="o", capsize=3, label="Mean ± SD")
    ax.set_xlabel("p")
    ax.set_ylabel(r"$\bar{k}$")
    ax.set_title("Average degree vs p", loc="left")
    ax.legend(loc="upper right", frameon=True)

    fig.tight_layout()
    fig.savefig(out_path, bbox_inches="tight")
    plt.show()
    plt.close(fig)


def main():
    # --- Setup argparse ---
    parser = argparse.ArgumentParser(
        description="Aggregate ER simulation outputs and plot metrics."
    )
    parser.add_argument(
        "--input-dir", type=str, default="results",
        help="Directory containing p_*.csv files (default: results)"
    )
    parser.add_argument(
        "--out-dir", type=str, default="figs",
        help="Directory to write summary CSV and figures (default: figs)"
    )
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    # --- Load & aggregate ---
    df = read_all_results(args.input_dir)
    summary = aggregate_by_p(df)

    # --- Plot figure ---
    plot_avg_degree(summary, os.path.join(args.out_dir, "avg_degree_vs_p.pdf"))

    print(f"Figure written: {args.out_dir}")


if __name__ == "__main__":
    main()

