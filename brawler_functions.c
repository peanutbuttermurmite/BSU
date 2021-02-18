#include <stdio.h>
#include "brawlstars_calculator.h"
#include "brawler_functions.h"

int powerPointsToLevel(struct brawler_t * brawler) {
  /**
   * powerPointsToLevel calculates the total amount
   * of Power Points to upgrade to the next level
   * @param brawler: Pointer to brawler_t structure.
   * @return: Power Points to next level upgrade.
   */

  if(brawler == ((struct brawler_t *) 0)) {
    // list is empty
    return -1;
  }

  int brawler_lvl = brawler->power_level;
  int brawler_pwr_pts = brawler->power_points;
  int rem_pwr_pts;

  switch(brawler_lvl) {
  case 1: {
    rem_pwr_pts = calcPowerPointsToLevel(brawler_pwr_pts, PWR_PTS_LVL_2);
  }
    break;
  case 2: {
    rem_pwr_pts = calcPowerPointsToLevel(brawler_pwr_pts, PWR_PTS_LVL_3);
  }
    break;
  case 3: {
    rem_pwr_pts = calcPowerPointsToLevel(brawler_pwr_pts, PWR_PTS_LVL_4);
  }
    break;
  case 4: {
    rem_pwr_pts = calcPowerPointsToLevel(brawler_pwr_pts, PWR_PTS_LVL_5);
  }
    break;
  case 5: {
    rem_pwr_pts = calcPowerPointsToLevel(brawler_pwr_pts, PWR_PTS_LVL_6);
  }
    break;
  case 6: {
    rem_pwr_pts = calcPowerPointsToLevel(brawler_pwr_pts, PWR_PTS_LVL_7);
  }
    break;
  case 7: {
    rem_pwr_pts = calcPowerPointsToLevel(brawler_pwr_pts, PWR_PTS_LVL_8);
  }
    break;
  case 8: {
    rem_pwr_pts = calcPowerPointsToLevel(brawler_pwr_pts, PWR_PTS_LVL_9);
  }
    break;
  case 9: {
    rem_pwr_pts = calcPowerPointsToLevel(brawler_pwr_pts, PWR_PTS_LVL_10);
  }
    break;
  default: {
    rem_pwr_pts = 0;
  }
    break;
  }

  return rem_pwr_pts;
}

int powerPointsToMax(struct brawler_t * brawler) {
  /**
   * powerPointsToMax calculates the amount of Power Points
   * required to reach the max level of a brawler through
   * Power Points - level 9.
   *
   * @param brawler: Brawler structure in observation.
   * @return: Power Points to level 9.
   */

  return calcPowerPointsCurr(PWR_PTS_LVL_10, 10) -
    calcPowerPointsCurr(brawler->power_points, brawler->power_level);
}


int calcPowerPointsToLevel(int curr_pwr_pts, int req_pwr_pts) {
  /**
   * calcPowerPointsRemain calculates the remaining Power Points
   * for a Brawler to upgrade to the next level based on the
   * given current Power Points and the Power Points goal.
   *
   * @param curr_pwr_pts: Brawler's current obtained Power Points.
   * @param req_pwr_pts: Power Points get to next level.
   * @return: Difference between the two values - zero if current is
   * larger than required.
   */

  if(curr_pwr_pts >= req_pwr_pts) {
    return 0;
  }
  else {
    return (req_pwr_pts - curr_pwr_pts);
  }
}

int calcPowerPointsCurr(int brawler_pwr_pts, int brawler_lvl) {
  /**
   * calcPowerPointsCurr calculates the total
   * accumulated Power Points of a brawler based on its
   * level and unspent Power Points.
   *
   * @param brawler_pwr_pts: Brawler's unspent Point Points.
   * @param brawler_lvl: Brawler's level.
   * @return: Total power points accumulated.
   */

  int power_points_sum = 0;
  int remaining_power_points;

  if(brawler_lvl >= 1) {
    power_points_sum += PWR_PTS_LVL_1;
  }
  if(brawler_lvl >= 2) {
    power_points_sum += PWR_PTS_LVL_2;;
  }
  if(brawler_lvl >= 3) {
    power_points_sum += PWR_PTS_LVL_3;
  }
  if(brawler_lvl >= 4) {
    power_points_sum += PWR_PTS_LVL_4;
  }
  if(brawler_lvl >= 5) {
    power_points_sum += PWR_PTS_LVL_5;
  }
  if(brawler_lvl >= 6) {
    power_points_sum += PWR_PTS_LVL_6;
  }
  if(brawler_lvl >= 7) {
    power_points_sum += PWR_PTS_LVL_7;
  }
  if(brawler_lvl >= 8) {
    power_points_sum += PWR_PTS_LVL_8;
  }
  if(brawler_lvl >= 9) {
    power_points_sum += PWR_PTS_LVL_9;
  }
  if(brawler_lvl >= 10) {
    power_points_sum += PWR_PTS_LVL_10;
  }

  power_points_sum += brawler_pwr_pts;
  return power_points_sum;
}

int calcPotentialLevel(int brawler_pwr_pts, int brawler_lvl) {
  /**
   * calcPotentialLevel calculates the potential level
   * that the Brawler could be assuming all Power Points were
   * spent to upgrade.
   * @param brawler_pwr_pts: Brawler's unspent Power Points.
   * @param brawler_lvl: Brawler's Power level.
   * @return: Brawler's potential level.
   */

  int potential_level;

  // highest level to smallest level
  if(brawler_pwr_pts >= calcPowerPointsCurr(PWR_PTS_LVL_9, 9)) {
    potential_level = 9;
  }
  else if(brawler_pwr_pts >= calcPowerPointsCurr(PWR_PTS_LVL_9, 8)) {
    potential_level = 8;
  }
  else if(brawler_pwr_pts >= calcPowerPointsCurr(PWR_PTS_LVL_7, 7)) {
    potential_level = 7;
  }
  else if(brawler_pwr_pts >= calcPowerPointsCurr(PWR_PTS_LVL_6, 6)) {
    potential_level = 6;
  }
  else if(brawler_pwr_pts >= calcPowerPointsCurr(PWR_PTS_LVL_5, 5)) {
    potential_level = 5;
  }
  else if(brawler_pwr_pts >= calcPowerPointsCurr(PWR_PTS_LVL_4, 4)) {
    potential_level = 4;
  }
  else if(brawler_pwr_pts >= calcPowerPointsCurr(PWR_PTS_LVL_3, 3)) {
    potential_level = 3;
  }
  else if(brawler_pwr_pts >= calcPowerPointsCurr(PWR_PTS_LVL_2, 2)) {
    potential_level = 2;
  }
  else {
    potential_level = 1;
  }

  return potential_level;
}

int coinsToLevel(struct brawler_t * brawler) {
  /**
   * coinsToLevel calculates the total amount
   * of Coins required to upgrade to the next level.
   * @param brawler: Pointer to brawler_t structure.
   * @return: Coins to next level.
   */

  if(brawler == ((struct brawler_t *) 0)) {
    return -1; // no brawlers in list
  }

  int coins;
  int level = brawler->power_level;

  switch(level) {
  case 1: {
    coins = COINS_LVL_2;
  }
    break;
  case 2: {
    coins = COINS_LVL_3;
  }
    break;
  case 3: {
    coins = COINS_LVL_4;
  }
    break;
  case 4: {
    coins = COINS_LVL_5;
  }
    break;
  case 5: {
    coins = COINS_LVL_6;
  }
    break;
  case 6: {
    coins = COINS_LVL_7;
  }
    break;
  case 7: {
    coins = COINS_LVL_8;
  }
    break;
  case 8: {
    coins = COINS_LVL_8;
  }
    break;
  case 9:
  case 10:
  default: {
    coins = 0;
  }
    break;
  }

  return coins;
}

int coinsToMax(struct brawler_t * brawler) {
  /**
   * coinsToMax calculates the amount of Coins
   * required to reach the max level of a brawler through
   * - level 9.
   *
   * @param brawler: Brawler structure in observation.
   * @return: Coins to level 9.
   */

  int coin_sum = 0;
  int level = brawler->power_level;

  if(level >= 1) {
    coin_sum += COINS_LVL_1;
  }
  if(level >= 2) {
    coin_sum += COINS_LVL_2;
  }
  if(level >= 3) {
    coin_sum += COINS_LVL_3;
  }
  if(level >= 4) {
    coin_sum += COINS_LVL_4;
  }
  if(level >= 5) {
    coin_sum += COINS_LVL_5;
  }
  if(level >= 6) {
    coin_sum += COINS_LVL_6;
  }
  if(level >= 7) {
    coin_sum += COINS_LVL_7;
  }
  if(level >= 8) {
    coin_sum += COINS_LVL_8;
  }
  if(level >= 9) {
    coin_sum += COINS_LVL_9;
  }
  if(level >= 10) {
    coin_sum += COINS_LVL_10;
  }

  coin_sum = 3090 - coin_sum;
  return coin_sum;
}
